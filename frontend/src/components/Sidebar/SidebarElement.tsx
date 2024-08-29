import React from 'react';
import { NavLink } from 'react-router-dom';


interface SidebarElementProps {
    label: string;
    icon?: React.ReactNode; // Assuming you're using something like FontAwesome icons
    path: string;
    pathname: string;
}

const SidebarElement: React.FC<SidebarElementProps> = ({ label, icon, path, pathname }) => {
    const [slashedElement, componentPath] = path.split('/');
    return (
        <li>
            <NavLink
                to={path}
                className={`group relative flex items-center gap-2.5 rounded-sm py-2 px-4 font-medium text-bodydark1 duration-300 ease-in-out hover:bg-graydark dark:hover:bg-meta-4 ${pathname.includes(componentPath) &&
                    'bg-graydark dark:bg-meta-4'
                    }`}
            >
                {icon && icon}
                {label}
            </NavLink>
        </li>
    );
};

export default SidebarElement;