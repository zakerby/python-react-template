import { useLogActions } from "../../data/actions/log.action";

interface RepositoryAnalysisStatusProps {
    handleAnalysis: () => void;
    analysisStatus: string;
}


const RepositoryAnalysisStatus = ({ handleAnalysis, analysisStatus }: RepositoryAnalysisStatusProps) => {
    const { logs, setLogs } = useLogActions();

    return (
        <div className="rounded-xs border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
            <div className="border-b border-stroke py-4 px-6.5 dark:border-strokedark">
                <h3 className="font-medium text-black dark:text-white">
                    Repo Analysis Status
                </h3>
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

                <div>
                    <label className="mb-3 block text-black dark:text-white">
                        Analysis logs
                    </label>
                    {
                        logs.map((log, index) => (
                            <div key={index} className="flex flex-col gap-2">
                                <div className="flex items-center space-x-2">
                                    <p className="text-gray-500 dark:text-gray-400 text-sm">
                                        {log.timestamp}
                                    </p>
                                    <p className="text-black dark:text-white text-sm">
                                        {log.message}
                                    </p>
                                </div>
                            </div>
                        ))
                    }
                </div>
            </div>
        </div>
    );
}

export default RepositoryAnalysisStatus;