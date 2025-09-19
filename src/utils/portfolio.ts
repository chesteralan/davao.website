import type { PaginateFunction } from 'astro';
import { cleanSlug } from './permalinks';
import type { Portfolio } from '~/types';
import { getCollection, type CollectionEntry } from 'astro:content';

let _portfolios: Array<Portfolio>;

const getNormalizedPortfolio = async (post: CollectionEntry<'portfolio'>): Promise<Portfolio> => {
  const { id, data } = post;

  const { publishDate: rawPublishDate = new Date(), title, excerpt, image, category, metadata } = data;

  const slug = cleanSlug(id);
  const publishDate = new Date(rawPublishDate);

  return {
    slug,
    publishDate,
    title,
    excerpt,
    image,
    category,
    metadata,
  };
};

const load = async function (): Promise<Array<Portfolio>> {
  const portfolios = await getCollection('portfolio');
  const normalizedPortfolios = portfolios.map(async (portfolio) => await getNormalizedPortfolio(portfolio));

  const results = (await Promise.all(normalizedPortfolios)).sort(
    (a, b) => b.publishDate.valueOf() - a.publishDate.valueOf()
  );

  return results;
};

export const fetchPortfolios = async (): Promise<Array<Portfolio>> => {
  if (!_portfolios) {
    _portfolios = await load();
  }

  return _portfolios;
};

export const getStaticPathsPortfolioList = async ({ paginate }: { paginate: PaginateFunction }) => {
  return paginate(await fetchPortfolios(), {
    params: { portfolio: 'portfolio' },
    pageSize: 6,
  });
};

export const getStaticPathsPortfolioPost = async () => {
  return (await fetchPortfolios()).flatMap((portfolio) => ({
    params: {
      portfolio: portfolio.slug,
    },
    props: { portfolio },
  }));
};
