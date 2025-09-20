import { getPermalink, getBlogPermalink, getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    {
      text: 'About',
      href: getPermalink('/about'),
    },
    {
      text: 'Services',
      href: getPermalink('/services'),
    },
    {
      text: 'Portfolio',
      href: getPermalink('/portfolio'),
    },
    {
      text: 'Blog',
      href: getBlogPermalink(),
    },
    {
      text: 'Contact',
      href: getPermalink('/contact'),
    },
  ],
  actions: [{ text: 'Sign Up', href: getPermalink('/sign-up') }],
};

export const footerData = {
  links: [
    {
      title: 'Services',
      links: [
        { text: 'Website Development', href: getPermalink('/services/website-development') },
        { text: 'Website Maintenance & Hosting', href: getPermalink('/services/website-maintenance-hosting') },
        { text: 'Custom Web Applications', href: getPermalink('/services/custom-web-applications') },
      ],
    },
    {
      title: 'Company',
      links: [
        { text: 'About', href: getPermalink('/about') },
        { text: 'Blog', href: getBlogPermalink() },
        { text: 'Services', href: getPermalink('/#services') },
        { text: 'Portfolio', href: getPermalink('/portfolio') },
      ],
    },
  ],
  secondaryLinks: [
    { text: 'Terms', href: getPermalink('/terms') },
    { text: 'Privacy Policy', href: getPermalink('/privacy') },
  ],
  socialLinks: [
    { ariaLabel: 'Facebook', icon: 'tabler:brand-facebook', href: 'https://www.facebook.com/dwds.ph/' },
    { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
    { ariaLabel: 'Github', icon: 'tabler:brand-github', href: 'https://github.com/davaowebsite' },
  ],
  footNote: `
    Made with ❤️ using <a class="text-blue-600 underline dark:text-muted" href="https://github.com/arthelokyo/astrowind" target="_blank"> AstroWind</a> by <a target="_blank" class="text-blue-600 underline dark:text-muted" href="https://alchie.cc"> Alchie</a> · All rights reserved.
  `,
};
