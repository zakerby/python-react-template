import { Navigate } from "react-router-dom";
import { useUserActions } from "../data/actions/user.action";

interface ProtectedRouteProps {
    children: React.ReactNode;
}

export const ProtectedRoute = ({ children }: ProtectedRouteProps) => {
    const {getToken} = useUserActions();

    if (!getToken()) {
        // user is not authenticated
        return <Navigate to="/auth/login" />;
    }
    return children; 
};