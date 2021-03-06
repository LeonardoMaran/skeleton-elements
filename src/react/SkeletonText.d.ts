import * as React from 'react';

interface SkeletonTextOptions extends React.HTMLAttributes<HTMLElement> {
  /**
   * HTML element tag
   *
   * @default 'span'
   */
  tag: string;

  /**
   * Animation effectt
   */
  effect: 'fade' | 'pulse' | 'blink';
}

declare const SkeletonText: React.FunctionComponent<SkeletonTextOptions>;

export default SkeletonText;
