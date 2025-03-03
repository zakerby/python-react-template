import {useAtom} from 'jotai';
import { useNavigate } from "react-router-dom";

import { projectAtom } from "../state/project";
import { userAtom } from "../state/user";

import { useProjectsRequest } from "../requests/useProjectsRequest";

export const useProjectActions = () => {
    const [user] = useAtom(userAtom);
    const [projects, setProjects] = useAtom(projectAtom);
    const navigate = useNavigate();
    const { getProjectsRequest, createProjectRequest, getProjectRequest, deleteProjectRequest } = useProjectsRequest();


    const fetchProjects = async () => {
        const fetchedProjects = await getProjectsRequest();
        setProjects(fetchedProjects);
    }

    const fetchProjectDetail = async (id: number) => {
        const project = await getProjectRequest(id);
        // check if project is already in the list and replace it
        let projectIndex = projects.findIndex((project) => project.id === id);
        if (projectIndex !== -1) {
            projects[projectIndex] = project;
            setProjects(projects);
        } else {
            setProjects([...projects, project]);
        }
    }

    const getProject = (id: number) => {
        let project = projects.find((project) => project.id === id);
        return project;
    }

    const createProject = async (projectName: string) => {
        const newProject = await createProjectRequest(projectName);
        setProjects([...projects, newProject]);
        navigate(`/view-project/${newProject.id}`);
    }

    const deleteProject = async (id: number) => {
        await deleteProjectRequest(id);
        setProjects(projects.filter((project) => project.id !== id));
        navigate('/');
    }

    const updateProject = (id: string, name: string, description: string) => {
    }

    return {
        projects,
        getProject,
        fetchProjects, fetchProjectDetail,
        createProject, deleteProject, updateProject,
    }
}