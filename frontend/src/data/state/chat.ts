import { atom } from 'jotai';

const chatAtom = atom([] as ChatMessage[]);

export { chatAtom }