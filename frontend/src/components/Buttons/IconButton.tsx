import { LucideIcon } from 'lucide-react';

interface IconButtonProps {
  icon: LucideIcon;
  text: string;
  onClick?: () => void;
}

const IconButton = ({ icon: Icon, text, onClick }: IconButtonProps) => {
  return (
    <button
      onClick={onClick}
      className="inline-flex items-center justify-center gap-2.5 rounded-full border border-primary py-4 px-10 text-center font-medium text-primary hover:bg-opacity-90 lg:px-8 xl:px-10"
    >
      <Icon />
      {text}
    </button>
  );
};

export default IconButton;
