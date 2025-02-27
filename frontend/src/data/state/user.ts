import { atom } from 'jotai';
import { User } from '../types/user';

const userAtom = atom({
    key: 'user',
    default: JSON.parse(localStorage.getItem('user')) as User | null
});


export { userAtom }