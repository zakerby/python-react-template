import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Trash, Pencil } from 'lucide-react';

import Breadcrumb from '../../components/Breadcrumbs/Breadcrumb';
import IconButton from '../../components/Buttons/IconButton';
import { useProjectActions } from '../../data/actions/project.action';
import CustomInput from '../../components/Forms/CustomInput';

const EditProject = () => {
  const { fetchProjectDetail, getProject, deleteProject } = useProjectActions();
  // get project detail from getProject using the id in the URL
  const { id: projectId } = useParams<{ id: string }>() as { id: string };
  const parsedId = parseInt(projectId);
  const project = getProject(parsedId);

  const pageName = `Project ${project?.name}`;

  const [projectName, setProjectName] = useState<string>('');

  const { updateProject } = useProjectActions();


  useEffect(() => {
    setProjectName(project?.name || '');
  }, [project]);

  const handleUpdateProjectBtnClick = () => {
    updateProject(parsedId, projectName);
  };


  return project && (
    <>
      <Breadcrumb pageName={pageName} />
      <div className="flex flex-col gap-9 pt-4">
        <div className="rounded-xs border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
          <div className="flex-1 p:2 sm:p-6 justify-between flex flex-col">
            {/* Section aligned to the right */}
            <div className="flex justify-between items-center">
            </div>
            <div className="flex flex-col gap-5.5 p-6.5">
              <CustomInput
                label="Project name"
                type="text"
                value={projectName}
                onChange={setProjectName}
                placeholder="Input a project name"
              />
              <button onClick={handleUpdateProjectBtnClick}
                className="flex w-full justify-center rounded-sm bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                Update project
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default EditProject;
