import { useState } from 'react';

import Breadcrumb from '../../components/Breadcrumbs/Breadcrumb';
import CustomInput from '../../components/Forms/CustomInput';

import { useProjectActions } from '../../data/actions/project.action';

const CreateProject = () => {
    const [projectName, setProjectName] = useState<string>('');
    const { createProject } = useProjectActions();

    const handleCreateProjectBtnClick = () => {
        createProject(projectName);
    };

    return (
        <>
            <Breadcrumb pageName="Create a new project" />

            <div className="grid grid-cols-1 gap-9 sm:grid-cols-1">
                <div className="flex flex-col gap-9">
                    <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
                        <div className="flex flex-col gap-5.5 p-6.5">
                            <CustomInput
                                label="Project name"
                                type="text"
                                value={projectName}
                                onChange={setProjectName}
                                placeholder="Input a project name"
                            />
                            <button onClick={handleCreateProjectBtnClick} className="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
                                Create project
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default CreateProject;
