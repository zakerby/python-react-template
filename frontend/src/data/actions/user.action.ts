import { useNavigate } from "react-router-dom";
import { useAtom } from 'jotai';
import { useLocalStorage } from '../helpers/useLocalStorage';
import { useAuthRequest } from '../requests/useAuthRequest';
import { useUserSettingsRequest } from '../requests/useUserSettingsRequest';
import { useUserNotificationsRequest } from '../requests/useUserNotificationsRequest';

import  {userAtom, tokenAtom} from '../state/user';

export const useUserActions = () => {
    const navigate = useNavigate();
    const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);
    const { loginRequest, registerRequest } = useAuthRequest();

    const  {getUserSettingsRequest, updateUserSettingsRequest} = useUserSettingsRequest();
    const {getUserNotificationsRequest} = useUserNotificationsRequest();

    const [user, setUser] = useAtom(userAtom);
    const [token, setToken] = useAtom(tokenAtom);

    const login = async (username: string, password: string) => {
        const { user, accessToken } = await loginRequest(username, password);
        const newUser = {
            ...user,
            accessToken
        };

        setToken(accessToken);
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

    const fetchUserNotifications = async () => {
        const userNotifications = await getUserNotificationsRequest();
        return userNotifications;
    }

    const getToken = () => {
        if(token == null) {
            // Try to get the token from the local storage
            const [storedAccessToken, setAccessToken, deleteAccessToken] = useLocalStorage('accessToken', null);
            if(storedAccessToken) {
                setToken(storedAccessToken);
            }
        }
        return token;
    }

    return { 
        user, login, logout, register, getToken,
        fetchUserSettings,  updateUserSettings,
        fetchUserNotifications
    };
}
