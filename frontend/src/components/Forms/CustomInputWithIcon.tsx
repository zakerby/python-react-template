import React from 'react';

interface InputWithIconProps extends React.InputHTMLAttributes<HTMLInputElement> {
    label: string;
    icon: React.ReactNode;
}

const InputWithIcon: React.FC<InputWithIconProps> = ({ label, icon, ...inputProps }) => {
    return (
        <div className="mb-4">
            <label className="mb-2.5 block font-medium text-black dark:text-white">
                {label}
            </label>
            <div className="relative">
                <input
                    {...inputProps}
                    className="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 text-black outline-hidden focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
                />
                <span className="absolute right-4 top-4">
                    {icon}
                </span>
            </div>
        </div>
    );
};

export default InputWithIcon;