import { atom } from 'recoil';
import { Project } from '../types/project';

const projectAtom = atom({
    key: 'project',
    default: [] as Project[]
});

export { projectAtom }