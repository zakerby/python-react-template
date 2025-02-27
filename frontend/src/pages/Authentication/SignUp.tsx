import React from 'react';
import { Link } from 'react-router-dom';

import { useUserActions } from '../../data/actions/user.action';
import InputWithIcon from '../../components/Forms/CustomInputWithIcon';
import LockIcon from '../../components/Icons/LockIcon';
import MailIcon from '../../components/Icons/MailIcon';
import UserIcon from '../../components/Icons/UserIcon';

const SignUp: React.FC = () => {
  const [username, setUsername] = React.useState('');
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [confirmPassword, setConfirmPassword] = React.useState('');

  const { register } = useUserActions();

  const handleSignUp = () => {
    register(username, password, confirmPassword, email);
  }

  return (
    <>
      <div className="rounded-xs border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark h-max">
        <div className="flex flex-wrap items-center justify-center h-max">
          <div className="w-full border-stroke dark:border-strokedark xl:w-1/2 xl:border-l-2">
            <div className="w-full p-4 sm:p-12.5 xl:p-17.5">
              <h2 className="mb-9 text-2xl font-bold text-black dark:text-white sm:text-title-xl2">
                Sign Up to LWCA
              </h2>

              <form>
                <InputWithIcon
                  label='Username'
                  onChange={(e) => setUsername(e.target.value)}
                  type="text"
                  placeholder="Enter your full name"
                  icon={<UserIcon />}
                />
                <InputWithIcon
                  label='Email'
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter your email"
                  type="email"
                  icon={<MailIcon />}
                />
                <InputWithIcon
                  label='Password'
                  onChange={(e) => setPassword(e.target.value)}
                  type="password"
                  placeholder="Enter your password"
                  icon={<LockIcon />}
                />
                <InputWithIcon
                  label='Re-type Password'
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  type="password"
                  placeholder="Re-enter your password"
                  icon={<LockIcon />}
                />
                <div className="mb-5">
                  <button
                    onClick={handleSignUp}
                    className="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 text-white transition hover:bg-opacity-90"
                  >
                    Create account
                  </button>
                </div>

                <div className="mt-6 text-center">
                  <p>
                    Already have an account?{' '}
                    <Link to="/auth/login" className="text-primary">
                      Sign in
                    </Link>
                  </p>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignUp;
