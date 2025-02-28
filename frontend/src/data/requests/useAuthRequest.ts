import { useAxios } from "../helpers/useAxios";

const AUTH_DOMAIN = 'auth';

export const useAuthRequest = () => {
    const { axiosBackend } = useAxios();

    const loginRequest = async (username: string, password: string) => {
        const response = await axiosBackend.post(`/${AUTH_DOMAIN}/login`, {
            username,
            password
        }).catch((error) => {
            throw new Error(error.response.data.message);
        });
        const { user, access_token: accessToken } = response.data;
        return {
            user,
            accessToken
        };
    }

    const registerRequest = async (username: string, email: string, password: string, confirmPassword: string) => {
        const response = await axiosBackend.post(`/${AUTH_DOMAIN}/register`, {
            username,
            email,
            password,
            confirm_password: confirmPassword
        });
        const { user, access_token: accessToken } = response.data;
        return {
            user,
            accessToken
        };
    }

    return {
        loginRequest,
        registerRequest
    }
}