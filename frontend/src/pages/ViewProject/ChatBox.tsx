import ChatInput from "./ChatBox/ChatInput";
import ChatMessage from "./ChatBox/ChatMessage";
import { useProjectActions } from "../../data/actions/project.action";
import { Project } from "../../data/types/project";

interface ChatBoxProps {
    project: Project;
}

const ChatBox = ({ project }: ChatBoxProps) => {
    const { queryLLM, chatMessages } = useProjectActions();
    const handleAddMessage = (message: string) => {
        queryLLM(project.id, message);
    };

    return (
        <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
            <div className="flex-1 p:2 sm:p-6 justify-between flex flex-col">
                <div 
                    id="messages" 
                    className="flex flex-col space-y-4 p-3 overflow-y-auto scrollbar-thumb-blue scrollbar-thumb-rounded scrollbar-track-blue-lighter scrollbar-w-2 scrolling-touch max-h-[500px]">
                    {
                        chatMessages.map(oneMessage =>
                            <ChatMessage
                                key={oneMessage.id}
                                message={oneMessage.message}
                                imgSrc={oneMessage.user.imageUrl}
                                imgAlt={oneMessage.user.name}
                                isCurrentUser={oneMessage.user.id === 1}
                            />
                        )
                    }
                    {
                        /* Add a label if the list of messages is empty */
                        chatMessages.length === 0 && (
                            <p className="text-center text-gray-400">You can communicate with a chatbot regarding the source of this project</p>
                        )
                    }
                </div>
                <ChatInput handleAddMessage={handleAddMessage} />
            </div>
        </div>
    );
}

export default ChatBox;