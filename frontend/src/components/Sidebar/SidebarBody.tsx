import React, { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';

import SidebarLinkGroup from './SidebarLinkGroup';
import SidebarElement from './SidebarElement';

import DashboardIcon from '../Icons/DashboardIcon';
import TableIcon from '../Icons/TableIcon';
import CalendarIcon from '../Icons/CalendarIcon';
import FormIcon from '../Icons/FormIcon';
import DropDownIcon from '../Icons/DropDownIcon';

import { useProjectActions } from '../../data/actions/project.action';
import ProjectSidebarLinkGroup from './ProjectSidebarLinkGroup';


const subSections = [
    {
        label: 'Ingest repository',
        path: '/ingest-repository'
    },
    {
        label: 'Ingest documentation',
        path: '/ingest-documentation'
    },
    {
        label: 'Chat',
        path: '/chat'
    }
]

interface SidebarBodyProps {
    sidebarExpanded: boolean;
    setSidebarExpanded: (arg: boolean) => void;
}

const SidebarBody = ({ sidebarExpanded, setSidebarExpanded }: SidebarBodyProps) => {
    const location = useLocation();
    const { pathname } = location;
    const { projects, fetchProjects } = useProjectActions();

    useEffect(() => {
        fetchProjects();
    }, []);


    return (
        <div className="no-scrollbar flex flex-col overflow-y-auto duration-300 ease-linear">
            {/* <!-- Sidebar Menu --> */}
            <nav className="mt-5 py-4 px-4 lg:mt-9 lg:px-6">
                {/* <!-- Menu Group --> */}
                <div>
                    <ul className="mb-6 flex flex-col gap-1.5">
                        {/* <!-- Menu Item Dashboard --> */}
                        <SidebarElement
                            label="Dashboard"
                            path="/"
                            pathname={pathname}
                            icon={<DashboardIcon />}
                        />
                        {/* <!-- Menu Item Dashboard --> */}
                        <SidebarElement
                            label="New project"
                            path="/create-project"
                            pathname={pathname}
                            icon={<TableIcon />}
                        />
                        {
                            projects.map((project, index) => (
                                <ProjectSidebarLinkGroup
                                    key={`project-${index}`}
                                    pathname={pathname}
                                    sidebarExpanded={sidebarExpanded}
                                    setSidebarExpanded={setSidebarExpanded}
                                    project={project}
                                />
                            ))
                        }
                    </ul>
                </div>
            </nav>
        </div>
    );
}

export default SidebarBody;