import { useParams } from 'react-router-dom';

import Breadcrumb from '../../../components/Breadcrumbs/Breadcrumb';
import RepositoryAnalysisForm from '../RepositoryAnalysisForm';
import { useProjectActions } from '../../../data/actions/project.action';

const logs = [
    {
        timestamp: '2021-09-21 12:00:00',
        message: 'Analysis started'
    },
    {
        timestamp: '2021-09-21 12:00:00',
        message: 'Analysis completed'
    }
]

const IngestRepositoryView = () => {
    const handleRepositoryIngest = () => {

    }
    const { getProject } = useProjectActions();

    const { id: projectId } = useParams<{ id: string }>();
    const parsedId = parseInt(projectId);
    const project = getProject(parsedId);

    const pageName = `Ingest repository`;

    return project && (
        <>
            <Breadcrumb pageName={pageName} />
            <div className="grid grid-cols-1 gap-9 sm:grid-cols-1">
                <div className="flex flex-col gap-12">
                    <RepositoryAnalysisForm
                        repoUrl={project.repository_url}
                        handleAnalysis={handleRepositoryIngest}
                    />
                    {/* Display logs */}
                    <div className='rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark'>
                        <div className='border-b border-stroke py-4 px-6.5 dark:border-strokedark'>
                            <h3 className='font-medium text-black dark:text-white'>
                                Analysis logs
                            </h3>
                        </div>
                        <div className='flex flex-col gap-2 p-6.5'>
                            {
                                logs.map((log, index) => (
                                    <div key={index} className='flex flex-col gap-2'>
                                        <div className='flex items-center space-x-2'>
                                            <p className='text-gray-500 dark:text-gray-400 text-sm'>
                                                {log.timestamp}
                                            </p>
                                            <p className='text-black dark:text-white text-sm'>
                                                {log.message}
                                            </p>
                                        </div>
                                    </div>
                                ))
                            }
                        </div>
                    </div>

                </div>
            </div>
        </>
    )
}

export default IngestRepositoryView;