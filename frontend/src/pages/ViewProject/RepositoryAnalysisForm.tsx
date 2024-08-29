import CustomInput from "../../components/Forms/CustomInput";

interface RepositoryAnalysisFormProps {
    repoUrl: string;
    handleAnalysis: () => void;
}

const RepositoryAnalysisForm = (props: RepositoryAnalysisFormProps) => {
    const { repoUrl, handleAnalysis } = props;

    return (
        <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
            <div className="border-b border-stroke py-4 px-6.5 dark:border-strokedark">
                <h3 className="font-medium text-black dark:text-white">
                    Repo Analysis Form
                </h3>
            </div>
            <div className="flex flex-col gap-5.5 p-6.5">
                <div className="flex flex-col gap-5.5 p-6.5">
                    <CustomInput
                        label="Git repository URL"
                        type="text"
                        value={repoUrl}
                        readOnly={true}
                        placeholder="Url of the repository to analyze"
                    />
                </div>
            </div>
            <div className="flex flex-col gap-5.5 p-6.5">
                <div className="flex justify-center">
                    <button
                        onClick={handleAnalysis}
                        className="inline-flex items-center justify-center rounded-full bg-primary py-4 px-5 text-center font-base text-white hover:bg-opacity-90 lg:px-8 xl:px-5"
                    >
                        Launch Repo Analysis
                    </button>
                </div>
            </div>
        </div>
    )
}

export default RepositoryAnalysisForm;