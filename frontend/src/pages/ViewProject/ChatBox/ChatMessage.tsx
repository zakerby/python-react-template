interface ChatMessageProps {
    message: string;
    imgSrc: string;
    imgAlt: string;
    isCurrentUser: boolean;
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message, imgSrc, imgAlt, isCurrentUser }) => {
    return (
        <div className="chat-message">
            <div className={`flex items-end ${isCurrentUser ? 'justify-end' : ''}`}>
                <div className={`flex flex-col space-y-2 text-base max-w-sm mx-2 ${isCurrentUser ? 'order-1 items-end' : 'order-2 items-start'}`}>
                    <div>
                        <span className={`px-4 py-2 rounded-lg inline-block ${isCurrentUser ? 'rounded-br-none bg-blue-600 text-white' : 'rounded-bl-none bg-gray-300 text-gray-600'}`}>
                            {message}
                        </span>
                    </div>
                </div>
                <img src={imgSrc} alt={imgAlt} className={`w-6 h-6 rounded-full ${isCurrentUser ? 'order-2' : 'order-1'}`} />
            </div>
        </div>
    );
};

export default ChatMessage;