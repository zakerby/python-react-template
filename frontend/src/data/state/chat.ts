import { atom } from 'jotai';

const chatAtom = atom({
    key: 'chat_message',
    default: [] as ChatMessage[]
});

export { chatAtom }