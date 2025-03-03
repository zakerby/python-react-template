import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Trash, Pencil } from 'lucide-react';


import Breadcrumb from '../../components/Breadcrumbs/Breadcrumb';

import { useProjectActions } from '../../data/actions/project.action';

const ViewProject = () => {
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
            {/* Section aligned to the right */}
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-bold text-primary dark:text-primarydark">
                {project.name}
              </h2>
              <div className="flex gap-2">
              <button 
                  className="inline-flex items-center justify-center gap-2.5 rounded-full border border-primary py-4 px-10 text-center font-medium text-primary hover:bg-opacity-90 lg:px-8 xl:px-10">
                  <Pencil />
                  Edit
                </button>
              <button 
                  className="inline-flex items-center justify-center gap-2.5 rounded-full border border-primary py-4 px-10 text-center font-medium text-primary hover:bg-opacity-90 lg:px-8 xl:px-10">
                  <Trash />
                  Delete
                </button>
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
