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
    if(!project) return;
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
      <div className="grid grid-cols-1 gap-9 sm:grid-cols-2">
        <div className="flex flex-col gap-12">
          <RepositoryAnalysisForm 
            repoUrl={project.repository_url} 
          />
        </div>

        <div className="flex flex-col gap-9">
          <RepositoryAnalysisStatus handleAnalysis={handleAnalysis} analysisStatus={analysisStatus} />
        </div>
      </div>

      <div className="flex flex-col gap-9 pt-4">
        <ChatBox project={project} />
      </div>
    </>
  );
};

export default ViewProject;
