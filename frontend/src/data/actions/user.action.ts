import { useRecoilState } from 'recoil';

import { userAtom } from '../state/user';
import { useLocalStorage } from '../helpers/useLocalStorage';
import { useAuthRequest } from '../requests/useAuthRequest';

export const useUserActions = () => {
    const [user, setUser] = useRecoilState(userAtom);
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);
    const { loginRequest, registerRequest } = useAuthRequest();

    const login = async (username: string, password: string) => {
        const { user, accessToken } = await loginRequest(username, password);
        const newUser = {
            ...user,
            accessToken
        };
        setAccessToken(accessToken);
        setUser(newUser);
    }

    const register = async (username: string, password: string, confirm_password: string, email: string) => {
        const { user, accessToken } = await registerRequest(username, email, password, confirm_password);
        const newUser = {
            ...user,
            accessToken
        };
        setAccessToken(accessToken);
        setUser(newUser);
    }

    const logout = () => {
        setUser(null);
        deleteAccessToken();
    }

    const getToken = () => {
        return storedAccessToken;
    }

    return { user, login, logout, register, getToken };
}
