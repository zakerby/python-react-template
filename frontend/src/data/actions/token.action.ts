import { useAtom } from 'jotai';

import  {tokenAtom} from '../state/user';
import { useLocalStorage } from '../helpers/useLocalStorage';

export const useTokenActions = () => {
    const [token, setTokenAtom] = useAtom(tokenAtom);
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);

    const getToken = () => {
        return token;
    }

    const setToken = (token: string) => {
        setTokenAtom(token);
        if (token !== null && token !== 'null') {
            setAccessToken(token);
        }
    }

    const removeToken = () => {
        setTokenAtom(null);
        deleteAccessToken();
    }

    return {
        getToken,
        setToken,
        removeToken
    }
};