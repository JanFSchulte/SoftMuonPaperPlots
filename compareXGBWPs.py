from numpy import array as ar
from setTDRStyle import setTDRStyle
import ROOT
from copy import deepcopy, copy

def main():
	
	canv = ROOT.TCanvas("c1","c1",800,800)
	
	#~ plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	#~ style = setTDRStyle()
	#~ gStyle.SetTitleYOffset(1.45)
	#~ gStyle.SetOptStat(0)
	#~ plotPad.UseCurrentStyle()
	#~ plotPad.Draw()	
	#~ plotPad.cd()
#~ 
	#~ resPad = TPad("resPad","resPad",0,0,1,0.3)
	#~ style = setTDRStyle()
	#~ gStyle.SetTitleYOffset(1.45)
	#~ gStyle.SetTitleXOffset(1.45)
	#~ gStyle.SetOptStat(0)
	#~ resPad.UseCurrentStyle()
	#~ resPad.Draw()	
	#~ resPad.cd()
	#~ resPad.SetGrid()
	plotPad = ROOT.TPad("plotPad","plotPad",0,0,1,1)
	#~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	#~ ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	#~ ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	#plotPad.SetGrid()
	ROOT.gStyle.SetTitleXOffset(1.45)
	ROOT.gStyle.SetTitleYOffset(1.5)



	ids = ["softMVARun3XGBSoft", "softMVARun3XGBLoose", "softMVARun3XGBMedium", "softMVARun3XGBTight"]
	idNames = {"softMVARun3XGBSoft": "XGB Soft", "softMVARun3XGBLoose": "XGB Loose", "softMVARun3XGBMedium": "XGB Medium", "softMVARun3XGBTight": "XGB Tight"}
	idColors = {"softMVARun3XGBSoft": ROOT.kMagenta, "softMVARun3XGBLoose": ROOT.kBlue, "softMVARun3XGBMedium": ROOT.kGreen+1, "softMVARun3XGBTight": ROOT.kRed}
	
	
	absetabins = ["1","2","3"]
	absetaLabels = {
		"1":"0 < |#eta| < 0.9",
		"2":"0.9 < |#eta| < 1.2",
		"3":"1.2 < |#eta| < 2.4",
	}
	
	eras = ["2022","2022_EE","2023","2023_BPix"]
	lumis = {"2022": 8.0, "2022_EE": 26.2, "2023": 17.7, "2023_BPix": 9.5}
	for era in eras:
		if era == "2022Fix":
			era = "2022"
		resultPath = "softMuonMVA%sNew/"%era
		mainPath = "plots/muon/generalTracks/JPsi/Run%s/NUM_%s_DEN_TrackerMuons/efficiency/"

		
		for abseta in absetabins:

			plotPad.cd()
			plotPad.SetLogx(0)
			plotPad.SetLogy(0)
			yMax = 1.2

			yLabel = 'Muon ID efficiency'
			plotPad.DrawFrame(0,0.,30,1.5,";probe muon p_{T} [GeV]; %s"%yLabel)


			leg = ROOT.TLegend(0.42, 0.72, 0.89, 0.92,"","brNDC")
			leg.SetFillColor(10)
			leg.SetFillStyle(0)
			leg.SetLineColor(10)
			leg.SetShadowColor(0)
		
			histsData = []
			histsMC = []
			for id in ids:
				
				f = ROOT.TFile(resultPath + mainPath%(era,id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")
				histsData.append(deepcopy(f.Get("g_0_Data").Clone(id)))
				histsMC.append(deepcopy(f.Get("g_1_Simulation").Clone(id+"MC")))
		
			for i in range(0,len(ids)):
				id = ids[i]
				histData = histsData[i]
				histMC = histsMC[i]
				histData.SetLineColor(idColors[id])
				histData.SetMarkerColor(idColors[id])
				histMC.SetLineColor(idColors[id]+2)
				histMC.SetMarkerColor(idColors[id]+2)
				histMC.SetLineStyle(ROOT.kDashed)
				histMC.SetMarkerStyle(21)

				leg.AddEntry(histData, idNames[id] + " Data", "pe")
				leg.AddEntry(histMC, idNames[id] + " MC", "pe")
				
				histData.Draw("samepe")
				histMC.Draw("samepe")

			latex = ROOT.TLatex()
			latex.SetTextFont(42)
			latex.SetTextAlign(31)
			latex.SetTextSize(0.04)
			latex.SetNDC(True)
			latexCMS = ROOT.TLatex()
			latexCMS.SetTextFont(61)
			latexCMS.SetTextSize(0.055)
			latexCMS.SetNDC(True)
			latexCMSExtra = ROOT.TLatex()
			latexCMSExtra.SetTextFont(52)
			latexCMSExtra.SetTextSize(0.03)
			latexCMSExtra.SetNDC(True) 
				
			latex.DrawLatex(0.95, 0.96, "%.1f fb^{-1} (13.6 TeV)"%lumis[era])
			
			cmsExtra = "#splitline{Preliminary}{}"
			latexCMS.DrawLatex(0.19,0.88,"CMS")
			if "Simulation" in cmsExtra:
				yLabelPos = 0.83	
			else:
				yLabelPos = 0.83	

			latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

			

			latex.DrawLatex(0.4,0.8,absetaLabels[abseta])		
			leg.Draw()	

			plotPad.RedrawAxis()
		


			canv.Print("SoftMuonEff_XGBWPs_abseta_%s_%s.pdf"%(abseta,era))
			canv.Print("SoftMuonEff_XGBWPs_abseta_%s_%s.png"%(abseta,era))
			
			
		
		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 1.2

		yLabel = 'Muon ID efficiency'
		plotPad.DrawFrame(-2.4,0.,2.4,1.5,";probe muon #eta; %s"%yLabel)


		leg = ROOT.TLegend(0.42, 0.72, 0.89, 0.92,"","brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)

		histsData = []
		histsMC = []
		for id in ids:
			
			f = ROOT.TFile(resultPath + mainPath%(era,id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")
			histsData.append(deepcopy(f.Get("g_0_Data").Clone(id)))
			histsMC.append(deepcopy(f.Get("g_1_Simulation").Clone(id+"MC")))

		for i in range(0,len(ids)):
			id = ids[i]
			histData = histsData[i]
			histMC = histsMC[i]
			histData.SetLineColor(idColors[id])
			histData.SetMarkerColor(idColors[id])
			histMC.SetLineColor(idColors[id]+2)
			histMC.SetMarkerColor(idColors[id]+2)
			histMC.SetLineStyle(ROOT.kDashed)
			histMC.SetMarkerStyle(21)

			leg.AddEntry(histData, idNames[id] + " Data", "pe")
			leg.AddEntry(histMC, idNames[id] + " MC", "pe")
			
			histData.Draw("samepe")
			histMC.Draw("samepe")

		latex = ROOT.TLatex()
		latex.SetTextFont(42)
		latex.SetTextAlign(31)
		latex.SetTextSize(0.04)
		latex.SetNDC(True)
		latexCMS = ROOT.TLatex()
		latexCMS.SetTextFont(61)
		latexCMS.SetTextSize(0.055)
		latexCMS.SetNDC(True)
		latexCMSExtra = ROOT.TLatex()
		latexCMSExtra.SetTextFont(52)
		latexCMSExtra.SetTextSize(0.03)
		latexCMSExtra.SetNDC(True) 
			
		latex.DrawLatex(0.95, 0.96, "%.1f fb^{-1} (13.6 TeV)"%lumis[era])
		
		cmsExtra = "#splitline{Preliminary}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.83	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		

		#latex.DrawLatex(0.4,0.8,absetaLabels[abseta])		
		leg.Draw()	

		plotPad.RedrawAxis()



		canv.Print("SoftMuonEff_XGBWPs_%s_vsEta.pdf"%(era))
		canv.Print("SoftMuonEff_XGBWPs_%s_vsEta.png"%(era))

	
	
main()
