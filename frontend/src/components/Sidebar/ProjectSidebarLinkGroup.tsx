import React from 'react';
import { NavLink } from 'react-router-dom';

import SidebarLinkGroup from './SidebarLinkGroup';

import DropDownIcon from '../Icons/DropDownIcon';
import TableIcon from '../Icons/TableIcon';
import { Project } from '../../data/types/project';

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
                        <div
                            className={`translate transform overflow-hidden ${!open && 'hidden'
                                }`}
                        >
                        </div>
                    </React.Fragment>
                );
            }}
        </SidebarLinkGroup>
    );
};

export default ProjectSidebarLinkGroup;