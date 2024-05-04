import type { Metadata } from "next";
import { Inter, Noto_Sans_KR } from "next/font/google";
import "./globals.css";
import Image from "next/image";
import { Button } from "@/components/ui/button";

const notoSans = Noto_Sans_KR({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "췍봇",
  description: "나만의 AI 웹 챗봇",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={notoSans.className}>
        <div className="fixed w-screen flex h-[80px] px-12 items-center justify-between backdrop-blur-sm z-[99]">
          <div className="flex items-center justify-center gap-4">
            <Image src="/icons/logo.png" width={48} height={48} alt="" />
            <div className="bold text-3xl">췍봇</div>
          </div>
          <div className="flex justify-center items-center gap-2">
            <Button variant="secondary">로그인</Button>
            <Button>회원가입</Button>
          </div>
        </div>
        {children}
      </body>
    </html>
  );
}
