import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import Breadcrumb from '../../components/Breadcrumbs/Breadcrumb';

import RepositoryAnalysisForm from './RepositoryAnalysisForm';
import RepositoryAnalysisStatus from './RepositoryAnalysisStatus';
import ChatBox from './ChatBox';
import { useProjectActions } from '../../data/actions/project.action';

const ViewProject = () => {
  const [analysisStatus, setAnalysisStatus] = useState<string>("Analysis status will be shown here");

  const handleAnalysis = () => {
    if (!project) return;
    setAnalysisStatus("Analysis in progress...");
  }

  const { fetchProjectDetail, getProject } = useProjectActions();
  // get project detail from getProject using the id in the URL
  const { id: projectId } = useParams<{ id: string }>();
  const parsedId = parseInt(projectId);
  const project = getProject(parsedId);
  useEffect(() => {
    fetchProjectDetail(parsedId);
  }, [projectId]);

  const pageName = `Project ${project?.name}`;

  return project && (
    <>
      <Breadcrumb pageName={pageName} />
      <div className="flex flex-col gap-9 pt-4">
        <div className="rounded-xs border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
          <div className="flex-1 p:2 sm:p-6 justify-between flex flex-col">
            <p className="text-center text-gray-400">
              Insert content here
              </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default ViewProject;
