import axios from 'axios';

import { FULL_URL } from '../requests/common';
import { useTokenActions } from '../actions/token.action';

export const useAxios = () => {
    const { getToken, removeToken } = useTokenActions();

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getToken()}`
    };

    const axiosBackend = axios.create({
        baseURL: FULL_URL,
        headers,
    });

    axiosBackend.interceptors.response.use((response) => {
        if (response.status === 200 || response.status === 201) {
            return response;
        } else {
            // error handling
            const messages = response.data.messages
            if (messages) {
              if (messages instanceof Array) {
                return Promise.reject({ messages });
              }
              return Promise.reject({ messages: [messages] });
            }
            return Promise.reject({ messages: ["got errors"] });
        }
    },
    (error) => {
        if(error.response) {
            if (error.response.status === 401) {
                // logout the user
                removeToken();
            }
        } 
    });

    return {
        axiosBackend
    }
}