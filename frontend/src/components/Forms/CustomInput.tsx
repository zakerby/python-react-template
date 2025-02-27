interface CustomInputProps {
    label: string;
    type: 'text' | 'file';
    value?: string;
    onChange: (value: any) => void;
    placeholder?: string;
    className?: string;
  }
  
  const CustomInput: React.FC<CustomInputProps> = ({ label, type, value, onChange, placeholder, className, ...otherProps }) => {
    const fileInputHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
      onChange(e.target.files?.[0] || null);
    };
  
    const textInputHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
      onChange(e.target.value);
    };
  
    return (
      <div>
        <label className={`mb-3 block text-black dark:text-white ${className}`}>
          {label}
        </label>
        {type === 'file' ? (
          <input
            type="file"
            onChange={fileInputHandler}
            className={`w-full rounded-md border border-stroke p-3 outline-hidden transition file:mr-4 file:rounded-sm file:border-[0.5px] file:border-stroke file:bg-[#EEEEEE] file:py-1 file:px-2.5 file:text-sm focus:border-primary file:focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-strokedark dark:file:bg-white/30 dark:file:text-white ${className}`}
            {...otherProps}
          />
        ) : (
          <input
            value={value}
            onChange={textInputHandler}
            type="text"
            placeholder={placeholder}
            className={`w-full rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-hidden transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary ${className}`}
          />
        )}
      </div>
    );
  };
  
  export default CustomInput;