import { useAxios } from "../helpers/useAxios";

const PROJECTS_DOMAIN = 'projects';
const PROJECT_DOMAIN = 'project';

export const useProjectsRequest = () => {
    const { axiosBackend } = useAxios();

    const getProjectsRequest = async () => {
        const response = await axiosBackend.get(`/${PROJECTS_DOMAIN}`);
        const fetchedProjects = response.data;
        return fetchedProjects;
    }
    
    const getProjectRequest = async (id: number) => {
        const response = await axiosBackend.get(`/${PROJECT_DOMAIN}/${id}`);
        const {data: project} = response;
        return project;
    }
    
    const createProjectRequest = async (projectName: string) => {
        const response = await axiosBackend.post(`/${PROJECTS_DOMAIN}`, {
            name: projectName,
        });
        const {project: newProject} = response.data;
        return newProject;
    }
    
    const deleteProjectRequest = async (id: number) => {
        const response = await axiosBackend.delete(`/${PROJECT_DOMAIN}/${id}`);
        return response.data;
    }
    
    

    return {
        getProjectsRequest,
        getProjectRequest,
        createProjectRequest,
        deleteProjectRequest
    }
}