import PageTitle from './components/PageTitle';
import SignIn from './pages/Authentication/SignIn';
import SignUp from './pages/Authentication/SignUp';
import Calendar from './pages/Calendar';
import Chart from './pages/Chart';
import ECommerce from './pages/Dashboard/ECommerce';
import FormElements from './pages/Form/FormElements';
import FormLayout from './pages/Form/FormLayout';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Tables from './pages/Tables';
import Alerts from './pages/UiElements/Alerts';
import Buttons from './pages/UiElements/Buttons';

import CreateProject from './pages/CreateProject/CreateProject';
import ViewProject from './pages/ViewProject/ViewProject';
import IngestRepositoryView from './pages/ViewProject/IngestRepositoryView/IngestRepositoryView';

const routes = [
    {
      path: '/',
      title: 'Dashboard | LWCA',
      component: <><PageTitle title="Dashboard | LWCA" /><ECommerce /></>,
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
      path: '/view-project/:id/ingest-repository',
      title: 'Ingest Repository | LWCA',
      component: <><PageTitle title="Ingest Repository | LWCA" /><IngestRepositoryView /></>,
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
      path: '/tables',
      title: 'Tables | LWCA',
      component: <><PageTitle title="Tables | LWCA" /><Tables /></>,
      isProtected: true
    },
    {
      path: '/settings',
      title: 'Settings | LWCA',
      component: <><PageTitle title="Settings | LWCA" /><Settings /></>,
      isProtected: true
    },
    {
      path: '/chart',
      title: 'Basic Chart | LWCA',
      component: <><PageTitle title="Basic Chart | LWCA" /><Chart /></>,
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