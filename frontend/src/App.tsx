import { useEffect, useState } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';
import { routes } from './routes';
import Loader from './common/Loader';

import AuthenticatedLayout from './layout/AuthenticatedLayout';
import UnauthenticatedLayout from './layout/UnauthenticatedLayout';
import { ProtectedRoute } from './layout/ProtectedRoute';
import { useTokenActions } from './data/actions/token.action';


function App() {
  const [loading, setLoading] = useState<boolean>(true);
  const { pathname } = useLocation();
  const {getToken} = useTokenActions();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1000);
  }, []);

  if (loading) {
    return <Loader />;
  }

  // get the auth context to check if the user is authenticated (based on the token)
  // if the user is authenticated, return the authenticated layout
  // otherwise, return the unauthenticated layout & redirect to the login page

  const CurrentLayout = getToken() !== null ? AuthenticatedLayout : UnauthenticatedLayout;

  return (
      <CurrentLayout>
        <Routes>
          {routes.map((route) => (
            <Route
              key={route.path}
              path={route.path}
              element={
                route.isProtected ? <ProtectedRoute>{route.component}</ProtectedRoute> : route.component
              }
            >
              {
                route.subRoutes && route.subRoutes.map((subRoute) => (
                  <Route
                    key={subRoute.path}
                    path={subRoute.path}
                    element={
                      route.isProtected ? <ProtectedRoute>{subRoute.component}</ProtectedRoute> : subRoute.component
                    }
                  />
                ))
              }
              </Route>
          ))}
        </Routes>
      </CurrentLayout>
  )
}

export default App;
