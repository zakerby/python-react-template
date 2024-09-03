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
        const response = await axiosBackend.delete(`/${PROJECTS_DOMAIN}/${id}`);
        return response.data;
    }
    
    const runProjectAnalysisRequest = async (id: number) => {
        // POST request to run analysis, parameter is either repoUrl or repoFolder
        const response = await axiosBackend.post(`/${PROJECT_DOMAIN}/${id}/analysis`);
        return response.data;
    }
    
    const queryLLMRequest = async (id: number, query: string) => {
        // POST request to run analysis, parameter is either repoUrl or repoFolder
        const response = await axiosBackend.post(`/${PROJECT_DOMAIN}/${id}/query_llm`, {
            query
        });
        const {data: {message}} = response;
        return message;
    }

    return {
        getProjectsRequest,
        getProjectRequest,
        createProjectRequest,
        deleteProjectRequest,
        runProjectAnalysisRequest,
        queryLLMRequest
    }
}