import { useAxios } from "../helpers/useAxios";

const USER_NOTIFICATIONS_DOMAIN = 'user/notifications';

export const useUserNotificationsRequest = () => {
    const { axiosBackend } = useAxios();

    const getUserNotificationsRequest = async () => {
        const response = await axiosBackend.get(`/${USER_NOTIFICATIONS_DOMAIN}`);
        const fetchedUserNotifications = response.data;
        return fetchedUserNotifications;
    }
    
    return {
        getUserNotificationsRequest
    }
}