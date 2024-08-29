interface ChatMessage {
    id: number;
    project_id: number;
    message: string;
    user: {
        id: number;
        name: string;
    };
}