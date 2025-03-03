import { useAtom } from 'jotai';

import  {tokenAtom} from '../state/user';
import { useLocalStorage } from '../helpers/useLocalStorage';

export const useTokenActions = () => {
    const [token, setTokenAtom] = useAtom(tokenAtom);
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);

    const getToken = () => {
        if(token == null) {
            // Try to get the token from the local storage
            if(storedAccessToken) {
                setToken(storedAccessToken);
            }
        }
        return token;
    }

    const setToken = (token: string) => {
        setTokenAtom(token);
        setAccessToken(token);
    }

    const removeToken = () => {
        setToken(null);
        deleteAccessToken();
    }

    return {
        getToken,
        setToken,
        removeToken
    }
};