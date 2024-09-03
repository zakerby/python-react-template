import { useRecoilState } from "recoil";
import { useNavigate } from "react-router-dom";

import { projectAtom } from "../state/project";
import { chatAtom } from "../state/chat";
import { userAtom } from "../state/user";

import { useProjectsRequest } from "../requests/useProjectsRequest";


export const useProjectActions = () => {
    const [user] = useRecoilState(userAtom);
    const [projects, setProjects] = useRecoilState(projectAtom);
    const [chatMessages, setChatMessages] = useRecoilState(chatAtom);
    const navigate = useNavigate();
    const { getProjectsRequest, createProjectRequest, getProjectRequest, queryLLMRequest } = useProjectsRequest();


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
        navigate(`/view-project/${newProject.id}/ingest-repository`);
    }

    const deleteProject = (id: string) => {
    }

    const updateProject = (id: string, name: string, description: string) => {
    }

    const queryLLM = async (id: string, query: string) => {
        const userMessage = {
            id: chatMessages.length + 1,
            project_id: parseInt(id),
            message: query,
            user: {
                id: user.id,
                name: user.name
            }
        };
        setChatMessages((currentChatMessages) => [...currentChatMessages, userMessage]);
        const message = await queryLLMRequest(parseInt(id), query);
        setChatMessages((currentChatMessages) => [...currentChatMessages, message]);
    }

    return {
        projects,
        chatMessages,
        getProject,
        fetchProjects, fetchProjectDetail,
        createProject, deleteProject, updateProject,
        queryLLM
    }
}