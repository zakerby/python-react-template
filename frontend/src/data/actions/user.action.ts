import { useNavigate } from "react-router-dom";
import { useAtom } from 'jotai';
import { useAuthRequest } from '../requests/useAuthRequest';
import { useUserSettingsRequest } from '../requests/useUserSettingsRequest';
import { useUserNotificationsRequest } from '../requests/useUserNotificationsRequest';

import  {userAtom} from '../state/user';
import { useTokenActions } from '../actions/token.action';

export const useUserActions = () => {
    const navigate = useNavigate();
    const { loginRequest, registerRequest } = useAuthRequest();
    const { getToken, removeToken, setToken } = useTokenActions();

    const  {getUserSettingsRequest, updateUserSettingsRequest} = useUserSettingsRequest();
    const {getUserNotificationsRequest} = useUserNotificationsRequest();

    const [user, setUser] = useAtom(userAtom);

    const login = async (username: string, password: string) => {
        const { user, accessToken } = await loginRequest(username, password);

        setToken(accessToken);
        setUser(user);
        navigate('/');
    }

    const register = async (username: string, password: string, confirm_password: string, email: string) => {
        const { user, accessToken } = await registerRequest(username, email, password, confirm_password);
        setToken(accessToken);
        setUser(user);
    }

    const logout = () => {
        setUser(null);
        removeToken();
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

    return { 
        user, login, logout, register, getToken,
        fetchUserSettings,  updateUserSettings,
        fetchUserNotifications
    };
}
