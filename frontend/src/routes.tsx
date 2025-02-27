import {lazy} from 'react';

import PageTitle from './components/PageTitle';

const Dashboard = lazy(() => import('./pages/Dashboard/Dashboard'));
const SignIn = lazy(() => import('./pages/Authentication/SignIn'));
const SignUp = lazy(() => import('./pages/Authentication/SignUp'));
const Calendar = lazy(() => import('./pages/Calendar'));
const FormElements = lazy(() => import('./pages/Form/FormElements'));
const FormLayout = lazy(() => import('./pages/Form/FormLayout'));
const Profile = lazy(() => import('./pages/Profile'));
const Settings = lazy(() => import('./pages/Settings'));
const Alerts = lazy(() => import('./pages/UiElements/Alerts'));
const Buttons = lazy(() => import('./pages/UiElements/Buttons'));

const CreateProject = lazy(() => import('./pages/CreateProject/CreateProject'));
const ViewProject = lazy(() => import('./pages/ViewProject/ViewProject'));

const routes = [
    {
      path: '/',
      title: 'Dashboard | LWCA',
      component: <><PageTitle title="Dashboard | LWCA" /><Dashboard /></>,
      isProtected: true
    },
    {
      path: '/create-project',
      title: 'Create Project | LWCA',
      component: <><PageTitle title="Create Project | LWCA" /><CreateProject /></>,
      isProtected: true
    },
    {
      path: '/view-project/:id',
      title: 'View Project | LWCA',
      component: <><PageTitle title="View Project | LWCA" /><ViewProject /></>,
      isProtected: true,
    },
    {
      path: '/calendar',
      title: 'Calendar | LWCA',
      component: <><PageTitle title="Calendar | LWCA" /><Calendar /></>,
      isProtected: true
    },
    {
      path: '/profile',
      title: 'Profile | LWCA',
      component: <><PageTitle title="Profile | LWCA" /><Profile /></>,
      isProtected: true
    },
    {
      path: '/forms/form-elements',
      title: 'Form Elements | LWCA',
      component: <><PageTitle title="Form Elements | LWCA" /><FormElements /></>,
      isProtected: true
    },
    {
      path: '/forms/form-layout',
      title: 'Form Layout | LWCA',
      component: <><PageTitle title="Form Layout | LWCA" /><FormLayout /></>,
      isProtected: true
    },
    {
      path: '/settings',
      title: 'Settings | LWCA',
      component: <><PageTitle title="Settings | LWCA" /><Settings /></>,
      isProtected: true
    },
    {
      path: '/ui/alerts',
      title: 'Alerts | LWCA',
      component: <><PageTitle title="Alerts | LWCA" /><Alerts /></>,
      isProtected: true
    },
    {
      path: '/ui/buttons',
      title: 'Buttons | LWCA',
      component: <><PageTitle title="Buttons | LWCA" /><Buttons /></>,
      isProtected: true
    },
    {
      path: '/auth/login',
      title: 'Signin | LWCA',
      component: <><PageTitle title="Signin | LWCA" /><SignIn /></>,
      isProtected: false
    },
    {
      path: '/auth/signup',
      title: 'Signup | LWCA',
      component: <><PageTitle title="Signup | LWCA" /><SignUp /></>,
      isProtected: false
    }
  ];

  export {routes};