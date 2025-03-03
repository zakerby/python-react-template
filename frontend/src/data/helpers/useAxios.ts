import axios from 'axios';
import { useAtom } from 'jotai';

import { FULL_URL } from '../requests/common';
import { useLocalStorage } from './useLocalStorage';

import  {tokenAtom} from '../atoms/user';

export const useAxios = () => {
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);
    const [token, setToken] = useAtom(tokenAtom);

    const getAuthHeader = () => {
        return token;
    }

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${getAuthHeader()}`
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
                deleteAccessToken();
            }
        } 
    });

    return {
        axiosBackend,
        getAuthHeader
    }
}