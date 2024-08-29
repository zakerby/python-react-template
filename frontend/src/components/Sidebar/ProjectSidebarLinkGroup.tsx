import React from 'react';
import { NavLink } from 'react-router-dom';

import SidebarLinkGroup from './SidebarLinkGroup';

import DropDownIcon from '../Icons/DropDownIcon';
import TableIcon from '../Icons/TableIcon';
import { Project } from '../../data/types/project';


const subSections = [
    {
        label: 'Ingest repository',
        path: 'ingest-repository'
    },
    {
        label: 'Ingest documentation',
        path: 'ingest-documentation'
    },
    {
        label: 'Projects files',
        path: 'project-files'
    },
    {
        label: 'Chat',
        path: 'chat'
    }
]

interface ProjectSidebarLinkGroupProps {
    pathname: string;
    sidebarExpanded: boolean;
    setSidebarExpanded: (expanded: boolean) => void;
    project: Project;
}

const ProjectSidebarLinkGroup: React.FC<ProjectSidebarLinkGroupProps> = ({
    pathname,
    sidebarExpanded,
    setSidebarExpanded,
    project
}) => {
    return (
        <SidebarLinkGroup
            activeCondition={
                pathname === '/project' || pathname.includes('project')
            }
        >
            {(handleClick, open) => {
                return (
                    <React.Fragment>
                        <NavLink
                            to="#"
                            className={`group relative flex items-center gap-2.5 rounded-sm py-2 px-4 font-medium text-bodydark1 duration-300 ease-in-out hover:bg-graydark dark:hover:bg-meta-4 ${(pathname === '/project' ||
                                pathname.includes('project')) &&
                                'bg-graydark dark:bg-meta-4'
                                }`}
                            onClick={(e) => {
                                e.preventDefault();
                                sidebarExpanded
                                    ? handleClick()
                                    : setSidebarExpanded(true);
                            }}
                        >
                            <TableIcon />
                            {project.name}
                            <DropDownIcon open={open} />
                        </NavLink>
                        {/* <!-- Dropdown Menu Start --> */}
                        <div
                            className={`translate transform overflow-hidden ${!open && 'hidden'
                                }`}
                        >
                            <ul className="mt-4 mb-5.5 flex flex-col gap-2.5 pl-6">
                                {subSections.map((subLink, index) => (
                                    <li key={`subSection-${index}`}>
                                        <NavLink
                                            to={`view-project/${project.id}/${subLink.path}`}
                                            className={({ isActive }) =>
                                                'group relative flex items-center gap-2.5 rounded-md px-4 font-medium text-bodydark2 duration-300 ease-in-out hover:text-white ' +
                                                (isActive && '!text-white')
                                            }
                                        >
                                            {subLink.label}
                                        </NavLink>
                                    </li>
                                ))}
                            </ul>
                        </div>
                        {/* <!-- Dropdown Menu End --> */}
                    </React.Fragment>
                );
            }}
        </SidebarLinkGroup>
    );
};

export default ProjectSidebarLinkGroup;