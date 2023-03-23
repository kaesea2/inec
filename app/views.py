from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,TemplateView,CreateView 
from .models import AnnouncedPuResults, PollingUnit,Lga
from .forms import LgaForm, PU_ResultForm

class Home(TemplateView):
    
    template_name = "app/index.html"

# Create your views here.

def pu_result(request, *args,**kwargs):
    if request.method == 'POST':
        form = LgaForm(request.POST)
        form2 = PU_ResultForm(request.POST)
        if form.is_valid():
            c_lga = form.cleaned_data['lga']
            lga = get_object_or_404(Lga, lga_name=c_lga)
            polling_unit = PollingUnit.objects.filter(lga_id__iexact=lga.lga_id)
            total = {}
            for pu in polling_unit:
                # print(pu.uniqueid)
                polling_unit_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__iexact=pu.uniqueid) 
                for pr in polling_unit_result:
                    party = pr.party_abbreviation
                    votes = pr.party_score
                    if party in total:
                        total[party] += votes
                    else:
                        total[party] = votes
            # print(total)
            return render(request, 'app/test.html', {'lga': c_lga, 'total': total})
        
        if form2.is_valid():
            party_score = form2.cleaned_data['party_score']
            print(party_score)
            polling_unit = form2.cleaned_data['polling_unit']
            print(polling_unit.polling_unit_id)
            party = form2.cleaned_data['party']
            print (party.partyname)
            # pu_id = 
            pu_result_add = AnnouncedPuResults.objects.create(polling_unit_uniqueid=polling_unit.polling_unit_id,
                                                              party_abbreviation=party.partyname,
                                                              party_score=party_score)
            pu_result_add.save()
            return render(request, 'app/test.html', {'polling_unit':polling_unit.polling_unit_id})
    # if request.method == 'GET':
    pu_id=request.GET.get('pu_id')
    if pu_id:
        result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__iexact=pu_id)  
        return render(request, 'app/test.html', {'pu_results':result,'pu_id':pu_id})

    form = LgaForm()
    form2 = PU_ResultForm()
    return render(request, 'app/index.html', {'form':form,'form2':form2})

   
# class PU_ResultCreateView(CreateView):
#     model = AnnouncedPuResults
#     template_name = "app/index.html"
#     form_class = PU_ResultForm
#     context_object_name = 'new_result'
