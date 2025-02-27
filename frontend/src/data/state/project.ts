import { atom } from 'jotai';
import { Project } from '../types/project';

const projectAtom = atom( [] as Project[]);

export { projectAtom }