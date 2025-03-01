import {useAtom} from 'jotai';

import { useNavigate } from "react-router-dom";

import { userAtom } from '../state/user';
import { useLocalStorage } from '../helpers/useLocalStorage';
import { useAuthRequest } from '../requests/useAuthRequest';
import { useUserSettingsRequest } from '../requests/useUserSettingsRequest';

export const useUserActions = () => {
    const navigate = useNavigate();
    const [user, setUser] = useAtom(userAtom);
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);
    const { loginRequest, registerRequest } = useAuthRequest();

    const  {getUserSettingsRequest, updateUserSettingsRequest} = useUserSettingsRequest();

    const login = async (username: string, password: string) => {
        const { user, accessToken } = await loginRequest(username, password);
        const newUser = {
            ...user,
            accessToken
        };
        setAccessToken(accessToken);
        setUser(newUser);
        navigate('/');
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
        // redirect to login
        navigate('/auth/login');
    }

    const fetchUserSettings = async () => {
        const userSettings = await getUserSettingsRequest();
        return userSettings;
    }

    const updateUserSettings = async (userSettings: any) => {
        const updatedUserSettings = await updateUserSettingsRequest(userSettings);
        return updatedUserSettings;
    }

    const getToken = () => {
        return storedAccessToken;
    }

    return { 
        user, login, logout, register, getToken,
        fetchUserSettings,  updateUserSettings
    };
}
