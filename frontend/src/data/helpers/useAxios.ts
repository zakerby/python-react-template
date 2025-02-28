import axios, { AxiosError, AxiosResponse } from 'axios';
import { FULL_URL } from '../requests/common';
import { useLocalStorage } from './useLocalStorage';

interface ErrorResponse {
  messages: string[];
  status?: number;
}

export const useAxios = () => {
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);

    const getAuthHeader = () => {
        return storedAccessToken;
    }

    // Create axios instance with improved config
    const axiosBackend = axios.create({
        baseURL: FULL_URL,
        headers: {
            'Content-Type': 'application/json',
        },
        timeout: 30000, // Add timeout to prevent hanging requests
    });

    // Apply auth token dynamically on each request
    axiosBackend.interceptors.request.use((config) => {
        // Get fresh token for each request
        if (storedAccessToken) {
            config.headers = {
                ...config.headers,
                'Authorization': `Bearer ${storedAccessToken}`
            };
        }
        return config;
    }, (error) => {
        return Promise.reject({
            messages: ['Request setup failed'],
            error
        });
    });

    // Handle responses and errors
    axiosBackend.interceptors.response.use(
        (response: AxiosResponse) => {
            if (response.status === 200 || response.status === 201) {
                return response;
            } else {
                // Handle unexpected success status codes
                const messages = response.data?.messages;
                if (messages) {
                    if (Array.isArray(messages)) {
                        return Promise.reject({ messages, status: response.status } as ErrorResponse);
                    }
                    return Promise.reject({ messages: [messages], status: response.status } as ErrorResponse);
                }
                return Promise.reject({ 
                    messages: [`Unexpected response status: ${response.status}`],
                    status: response.status 
                } as ErrorResponse);
            }
        },
        (error: AxiosError) => {
            // Handle request cancellation
            if (axios.isCancel(error)) {
                return Promise.reject({ messages: ['Request was cancelled'] });
            }

            // Handle timeout
            if (error.code === 'ECONNABORTED') {
                return Promise.reject({ 
                    messages: ['The request took too long to complete. Please try again.'] 
                });
            }

            // Handle network errors
            if (!error.response) {
                return Promise.reject({ 
                    messages: ['Network error. Please check your connection.'] 
                });
            }

            // Handle authentication errors
            if (error.response.status === 401) {
                deleteAccessToken();
                return Promise.reject({
                    messages: ['Your session has expired. Please log in again.'],
                    status: 401
                });
            }

            // Handle server errors
            if (error.response.status >= 500) {
                return Promise.reject({
                    messages: ['Server error. Please try again later.'],
                    status: error.response.status
                });
            }

            // Handle other API errors
            const errorData = error.response.data;
            if (errorData) {
                if (errorData.messages) {
                    const messages = Array.isArray(errorData.messages) 
                        ? errorData.messages 
                        : [errorData.messages];
                    return Promise.reject({ 
                        messages, 
                        status: error.response.status 
                    });
                } 
                
                if (errorData.message) {
                    return Promise.reject({ 
                        messages: [errorData.message], 
                        status: error.response.status 
                    });
                }
            }

            // Fallback error
            return Promise.reject({ 
                messages: [`Error ${error.response.status}: ${error.message || 'Unknown error'}`],
                status: error.response.status 
            });
        }
    );

    // Helper for retrying failed requests
    const retryRequest = async (requestFn, maxRetries = 3, delayMs = 1000) => {
        let lastError;
        
        for (let attempt = 0; attempt < maxRetries; attempt++) {
            try {
                return await requestFn();
            } catch (error) {
                // Only retry on network errors or server errors (5xx)
                const isRetryable = !error.status || error.status >= 500;
                if (!isRetryable || attempt === maxRetries - 1) {
                    throw error; // Don't retry or max retries reached
                }
                
                lastError = error;
                // Exponential backoff
                await new Promise(resolve => setTimeout(resolve, delayMs * Math.pow(2, attempt)));
            }
        }
        
        throw lastError;
    };

    return {
        axiosBackend,
        getAuthHeader,
        retryRequest
    }
}