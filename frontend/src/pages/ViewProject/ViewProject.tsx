import { useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Trash, Pencil } from 'lucide-react';

import Breadcrumb from '../../components/Breadcrumbs/Breadcrumb';
import IconButton from '../../components/Buttons/IconButton';
import { useProjectActions } from '../../data/actions/project.action';

const ViewProject = () => {
  const { fetchProjectDetail, getProject, deleteProject } = useProjectActions();
  const navigate = useNavigate();
  // get project detail from getProject using the id in the URL
  const { id: projectId } = useParams<{ id: string }>()  as { id: string };
  const parsedId = parseInt(projectId);
  const project = getProject(parsedId);

  useEffect(() => {
    fetchProjectDetail(parsedId);
  }, [projectId]);

  const handleDeleteProjectBtnClick = () => {
    // delete project
    deleteProject(parsedId);
  };

  const handleEditProjectBtnClick = () => {
    // navigate to edit project page
    navigate(`/edit-project/${parsedId}`);
  };

  const pageName = `Project ${project?.name}`;

  return project && (
    <>
      <Breadcrumb pageName={pageName} />
      <div className="flex flex-col gap-9 pt-4">
        <div className="rounded-xs border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
          <div className="flex-1 p:2 sm:p-6 justify-between flex flex-col">
            {/* Section aligned to the right */}
            <div className="flex justify-between items-center">
              <div className="flex gap-2">
                <IconButton icon={Pencil} text="Edit" onClick={handleEditProjectBtnClick}/>
                <IconButton icon={Trash} text="Delete" onClick={handleDeleteProjectBtnClick} />
              </div>
            </div>
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
