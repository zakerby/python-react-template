import { atom } from 'recoil';

const tokenAtom = atom({
    key: 'token',
    default: null as string | null

});

export {tokenAtom};