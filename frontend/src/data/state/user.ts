import { atom } from 'jotai';
import { User } from '../types/user';

const userAtom = atom({
    key: 'user',
    default: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user') as string) as User : null
});


export { userAtom }