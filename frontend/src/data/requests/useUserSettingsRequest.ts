import { useAxios } from "../helpers/useAxios";

const USER_SETTINGS_DOMAIN = 'user_settings';

export const useUserSettingsRequest = () => {
    const { axiosBackend } = useAxios();

    const getUserSettingsRequest = async () => {
        const response = await axiosBackend.get(`/${USER_SETTINGS_DOMAIN}`);
        const fetchedUserSettings = response.data;
        return fetchedUserSettings;
    }
    
    const updateUserSettingsRequest = async (userSettings: any) => {
        const response = await axiosBackend.put(`/${USER_SETTINGS_DOMAIN}`, userSettings);
        const updatedUserSettings = response.data;
        return updatedUserSettings;
    }

    return {
        getUserSettingsRequest,
        updateUserSettingsRequest
    }
}