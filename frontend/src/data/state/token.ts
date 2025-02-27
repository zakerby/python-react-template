import { atom } from 'jotai';

const tokenAtom = atom({
    key: 'token',
    default: null as string | null

});

export {tokenAtom};