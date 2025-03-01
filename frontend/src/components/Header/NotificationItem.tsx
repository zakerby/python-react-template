import { Link } from 'react-router-dom';

interface NotificationItemProps {
    title: string;
    message: string;
    date: string;
}

const NotificationItem: React.FC<NotificationItemProps> = ({ title, message, date }) => (
    <li>
        <Link
            className="flex flex-col gap-2.5 border-t border-stroke px-4.5 py-3 hover:bg-gray-2 dark:border-strokedark dark:hover:bg-meta-4"
            to="#"
        >
            <p className="text-sm">
                <span className="text-black dark:text-white">{title}</span> {message}
            </p>
            <p className="text-xs">{date}</p>
        </Link>
    </li>
);

export default NotificationItem;
